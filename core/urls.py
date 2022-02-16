from django.urls import path
from core import views


urlpatterns = [
    path('stock_history_key_ratio_json', views.stock_history_key_ratio_json, name='home'),
    path('stock_income_statement_json', views.income_statement_json, name='home'),
]