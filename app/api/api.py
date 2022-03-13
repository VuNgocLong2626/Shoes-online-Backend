from fastapi import APIRouter
from app.api.routers import permission, name_services, user, admin, gender, promotion


router = APIRouter()


router.include_router(permission.router)
router.include_router(name_services.router)
router.include_router(user.router)
router.include_router(admin.router)
router.include_router(gender.router)
router.include_router(promotion.router)
