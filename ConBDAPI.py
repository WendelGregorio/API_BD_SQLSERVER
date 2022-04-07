def Dados():
    import pyodbc
    
    projetos = {} #dicionário para armazenar dados do bancp
    
    Conn = pyodbc.connect('Driver={SQL Server};'
                            'Server="SEU SERVIDOR";'
                            'Database="SEU BANCO DE DADOS";'
                            'Trusted_Connection=yes;')
    
    cursor = Conn.cursor() #CURSOR PARA DADOS DO BANCO
    cursor.execute("select top * from SUA TABELA") # CURSOS FAZENDO CONSULTA NO BANCO
    
    while 1: #LAÇO PARA RECUPERAR DADOS ESPECIFICOS DO BANCO E ARMAZENAR EM PROJETOS
        row = cursor.fetchone()
        if not row:
            break
        projetos[row.ID] = {row.IDUSUARIO_SOLICITACAO, row.PRODUTO, row.DT_APROVADO}     
    cursor.close()
    Conn.close()
    return projetos # RETORNA O DICIONÁRIO COM TODOS OS DADOS