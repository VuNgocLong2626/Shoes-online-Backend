from fastapi import APIRouter
from app.services import athu, customers
from app.models.schemas import athu, customers as _customer_schemas


router = router = APIRouter(
    tags=["/user"],
    responses={404: {"description": "Not found"}}
)



@router.post(
    "/create-user",
    response_model=_customer_schemas.CustomerDetail)
async def create_user(
    user_in = _customer_schemas.CustomerCreate
):
    return {"ahihi"}