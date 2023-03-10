SELECT
  E1.EMP_ID AS EMP_ID,
  E1.EMP_NAME AS EMP_NAME,
  ISNULL(E2.EMP_NAME, 'CEO') AS MANAGER_NAME
FROM EMPLOYEES AS E1
LEFT INNER JOIN EMPLOYEES AS E2
ON E1.MGR_ID = E2.EMP_ID;
