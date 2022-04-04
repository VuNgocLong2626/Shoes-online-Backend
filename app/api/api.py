from fastapi import APIRouter
from app.api.routers import permission, name_services, user, admin, gender, promotion, color, size, category, product, file, bill, rate, rate_comment, services, payment


router = APIRouter()


router.include_router(permission.router)
router.include_router(name_services.router)
router.include_router(user.router)
router.include_router(admin.router)
router.include_router(gender.router)
router.include_router(promotion.router)
router.include_router(color.router)
router.include_router(size.router)
router.include_router(category.router)
router.include_router(product.router)
router.include_router(file.router)
router.include_router(bill.router)
router.include_router(rate.router)
router.include_router(rate_comment.router)
router.include_router(services.router)
router.include_router(payment.router)