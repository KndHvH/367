
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

/
DECLARE
    v_soma_sal  NUMBER;
    v_deptno    NUMBER NOT NULL := 20;
BEGIN
    SELECT SUM(SAL)
    INTO v_soma_sal
    from EMP
    WHERE deptno = v_deptno;
DBMS_OUTPUT.PUT_LINE('A soma dos salários do departamento ' ||v_deptno||' é '||v_soma_sal);
END;
/







/
select 'alter system kill session ''' || s.sid || ',' || s.serial# || ',@' || s.inst_id || ''' immediate;' cmd
 ,      s.username
 ,      o.object_name
 ,      s.sid
 ,      s.serial#
 ,      s.inst_id
 ,      p.spid
 ,      s.program
 ,      s.machine
 ,      s.osuser
 ,      s.port
 ,      s.logon_time
 ,      sq.sql_text
 from   gv$locked_object l
 ,      dba_objects      o
 ,      gv$session       s
 ,      gv$process       p
 ,      gv$sql           sq
 where  o.object_id = l.object_id
 and    s.sid = l.session_id
 and    s.inst_id = l.inst_id
 and    p.addr = s.paddr
 and    sq.address(+) = s.sql_address
 order by s.username
 ,      s.inst_id
 ,      s.sid
 ,      s.serial#
 ,      o.object_name;

/