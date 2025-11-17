from analytics.analytics_module import AnalyticsService
from database.db_connection import DBConnection

db = DBConnection("mysql:3036")

db.connect()

analytics = AnalyticsService(db)

print(f"Sum of sales : {analytics.sum_of_sales()}")
print(f"Average of sales : {analytics.avg_of_sales()}")

db.closeConnection()