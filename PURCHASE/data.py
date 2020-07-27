from PURCHASE.models import *

Supplier.objects.create(name="Apple Inc.", supplier_type=SupplierType.objects.get(id=1), description="Apple products help employees work more simply and productively, solve problems creatively, and collaborate with a shared purpose. And they’re all designed to work together beautifully. When people have the power to work the way they want, with the tools they love, they can do their best work.", email="info@apple.com", website="https://apple.com")

Supplier.objects.create(name="Microsoft Inc.", supplier_type=SupplierType.objects.get(id=1), description="At Microsoft we are dedicated to advancing human and organizational achievement.", email="info@microsoft.com", website="https://www.microsoft.com")

Supplier.objects.create(name="Google Inc.", supplier_type=SupplierType.objects.get(id=1), description="Our mission is to organize information in this world and make it accessible anywhere and useful.", email="info@google.com", website="https://www.google.com")


