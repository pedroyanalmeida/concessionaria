-- ------------------------------------------
-- TOP 3 vendedores com mais vendas
-- ------------------------------------------
SELECT 
    vd.Nome AS Vendedor,
    COUNT(v.Num_venda) AS Total_Vendas
FROM VENDA AS v
JOIN Vendedor AS vd
    ON v.Vendedor_CPF = vd.CPF
WHERE YEAR(v.Data) = 2026
GROUP BY vd.CPF, vd.Nome
ORDER BY Total_Vendas DESC
LIMIT 3;

-- ------------------------------------------
-- TOP 3 modelos mais vendidos
-- ------------------------------------------

SELECT
	mo.Nome AS Modelo, 
    ma.Nome AS Marca,
    COUNT(c.Chasse) AS Total_Vendas
    FROM Carros AS c
    JOIN Modelo AS mo
		ON c.Modelo_idModelo = mo.idModelo
    JOIN Marca AS ma
		ON mo.Marca_CNPJ = ma.CNPJ
    JOIN VENDA AS vd
		ON c.VENDA_Num_venda = vd.Num_venda
	GROUP BY ma.Nome, mo.Nome
    ORDER BY Total_Vendas DESC  
    LIMIT 3;
    
-- ----------------------------------------
-- CARROS DO MENOR AO MAIOR PREÇO 
-- ----------------------------------------

SELECT 
	c.Preço,
    mo.Nome AS Modelo,
    ma.Nome AS Marca,
    c.Cor,
    mo.Ano_Modelo
    FROM Carros As c
    JOIN Modelo AS mo
		ON c.Modelo_idModelo = mo.idModelo
	JOIN Marca AS ma
		ON mo.Marca_CNPJ = ma.CNPJ
	ORDER BY c.Preço ASC;
    
		