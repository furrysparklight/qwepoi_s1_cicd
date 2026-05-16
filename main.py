from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from pydantic import BaseModel

# Отключаем дефолтный Swagger при инициализации (docs_url=None)
app = FastAPI(title="Math & String API", docs_url=None, redoc_url=None)

class MathRequest(BaseModel):
    number: float

class StringRequest(BaseModel):
    text: str

@app.post("/math/double")
async def double_number(data: MathRequest):
    return {"result": data.number * 2}

@app.post("/string/uppercase")
async def to_uppercase(data: StringRequest):
    return {"result": data.text.upper()}

# Кастомный роут для Swagger, который стабильно работает через прокси
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css",
    )
