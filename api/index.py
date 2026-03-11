from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import datetime
from chinese_calendar import is_workday

# 初始化 FastAPI 实例
app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")

# 定义前端传入的数据格式
class CalcRequest(BaseModel):
    start_date: str
    days: int

@app.post("/api/calculate")
def calculate_dates(req: CalcRequest):
    if req.days <= 0:
        raise HTTPException(status_code=400, detail="工作日天数必须大于 0")

    try:
        current_date = datetime.datetime.strptime(req.start_date, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式错误，请使用 YYYY-MM-DD")

    try:
        days_remaining = req.days
        end_date = current_date

        # 计算截止日期
        while days_remaining > 0:
            if is_workday(end_date):
                days_remaining -= 1
                if days_remaining == 0:
                    break
            if days_remaining > 0:
                end_date += datetime.timedelta(days=1)

        # 计算下一个工作日
        next_workday = end_date + datetime.timedelta(days=1)
        while not is_workday(next_workday):
            next_workday += datetime.timedelta(days=1)

        return {
            "start_date": req.start_date,
            "required_days": req.days,
            "end_date": end_date.strftime("%Y-%m-%d"),
            "next_workday": next_workday.strftime("%Y-%m-%d")
        }
        
    except NotImplementedError as e:
        raise HTTPException(status_code=500, detail=f"日历库需更新，暂不支持该年份: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))