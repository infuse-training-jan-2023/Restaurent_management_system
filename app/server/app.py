from fastapi import FastAPI
from server.routes.cart_routes import router as cart_router
from server.routes.checkout_routes import router as checkout_router
from server.routes.table_routes import router as table_router
from server.routes.item_routes import router as item_router

app = FastAPI()

app.include_router(cart_router, tags=["Cart"], prefix="/cart")
app.include_router(checkout_router, tags=["Checkout"], prefix="/checkout")
app.include_router(table_router, tags=["Tables"], prefix="/tables")
app.include_router(item_router, tags=["Items"], prefix="/items")
