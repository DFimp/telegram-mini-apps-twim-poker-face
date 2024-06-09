from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter(prefix="/pages", tags=["Pages"])

templates = Jinja2Templates(directory="server/src/templates")


@router.get("/")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


@router.get("/table")
def get_table_page(request: Request):
    return templates.TemplateResponse("table.html", {"request": request})
