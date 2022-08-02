
SELECT * FROM EMP

/
DECLARE
  v_nome    VARCHAR2(30);
  v_cargo   VARCHAR2(30);
BEGIN
  SELECT ename, job
  INTO v_nome, v_cargo
  FROM emp
  WHERE empno = 7934;
DBMS_OUTPUT.PUT_LINE(v_nome);
DBMS_OUTPUT.PUT_LINE(v_cargo);
END;
/
/
DECLARE
    v_nome VARCHAR2(30);
    v_job VARCHAR2(30);
BEGIN
    SELECT ename,job
    INTO v_nome, v_job
    FROM EMP
    WHERE EMPNO = 7844;
DBMS_OUTPUT.PUT_LINE(v_nome);
DBMS_OUTPUT.PUT_LINE(v_job);
END;
/
