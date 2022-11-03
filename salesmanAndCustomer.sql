SELECT * from Salesman as S INNER JOIN Customer as C on(S.salesman_id = C.salesman_id)   
where S.city = 'London'
