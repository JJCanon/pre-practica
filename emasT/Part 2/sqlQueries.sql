-- get all items that are allow
SELECT * FROM items WHERE lent = 0

-- get all items that are currently lent
SELECT * FROM items where lent = 1

-- calculate the mos lent item
SELECT items.id, items.title, COUNT(loans.id) AS times_lent
FROM items
JOIN loans ON items.id = loans.item_id
GROUP BY items.id
ORDER BY times_lent DESC
LIMIT 1;