-- SQLite
-- --Obtenga todos los productos almacenados
SELECT * FROM products

-- --Obtenga todos los productos que tengan un precio mayor a 50000

SELECT * FROM products WHERE price > 50000

-- Obtenga todas las compras de un mismo producto por id.
SELECT * FROM invoice_product WHERE product_id = 1;

--Obtenga todas las compras agrupadas por producto, donde se muestre el total comprado entre todas las compras.
SELECT product_id, SUM(total_amount) FROM invoice_product GROUP BY product_id 

--Obtenga todas las facturas realizadas por el mismo comprador
SELECT * FROM invoices WHERE buyer_email = 'cust1@example.com'

--Obtenga todas las facturas ordenadas por monto total de forma descendente
SELECT * FROM invoices ORDER BY total_amount DESC;

--Obtenga una sola factura por número de factura.
SELECT * FROM invoices WHERE invoice_number = 'INV001';