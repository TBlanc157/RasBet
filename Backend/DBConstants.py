class DBConstants:
    add_sport       = 'INSERT INTO Jogo(nomeDesporto) VALUES((%s));'
    add_team        = 'INSERT INTO EquipasPorJogo(nomeEquipa, idJogo, Odd, jogaEmCasa) VALUES((%s),(%s),(%s),(%s));'
    register_user   = 'INSERT INTO Utilizador (email,password,idCarteira,dataNascimento,nif) VALUES ((%s),(%s),(%s),(%s),(%s));'
    get_log_info    = 'SELECT email, password FROM Utilizador WHERE email=(%s);'
    add_wallet      = 'INSERT INTO Carteira (saldoCarteira) VALUES(0.00);'
    get_sports      = 'SELECT DISTINCT nomeDesporto FROM Jogo;'
    get_by_sport    = 'SELECT idJogo FROM Jogo WHERE nomeDesporto = (%s);'
    get_game_info   = 'SELECT nomeEquipa, Odd, jogaEmCasa FROM EquipasPorJogo WHERE idJogo = (%s);'
