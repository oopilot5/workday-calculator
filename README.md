## README
工作日排期计算
选择开始日期 和 所需工作日，给出截止日期和下一个工作日。 自动计算周末、中国法定节假日和补班。

项目目录结构
workday-calculator/
├── api/
│   └── index.py        # FastAPI 后端逻辑
├── index.html          # 前端网页UI
├── requirements.txt    # Python 依赖清单
└── vercel.json         # Vercel 部署配置文件

Vercel 部署 (前后端分离的 Serverless 架构)
把 Python 作为无服务器函数 (Serverless Functions) 来运行，免费额度高。
将 Python 脚本用 FastAPI 或 Flask 包装成 API 接口，放在项目的 /api 目录下。

框架: 前端 html + 后端 python + fastapi  Serverless 

### 本地运行方式 -- 使用 Vercel CLI
```bash
npm i -g vercel
vercel dev
```
启动后，它会在本地 localhost:3000 完美模拟 Vercel 的线上环境，前后端路由自动生效，你修改代码保存后还会热更新！