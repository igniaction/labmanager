CREATE TABLE chemical_abstract_service (
    element_id integer primary key autoincrement,
    formula text not null,
    nomenclatura text not null,
    numero_cas text not null
);




CREATE TABLE reagentes (
    reagente_id integer primary key autoincrement,
    reagente_nome text not null,
    reagente_simbolo text not null,
    reagente_numero_atomico text not null,
    reagente_massa_atomica text not null,
    reagente_distribuicao_eletronica text not null,
    
);


CREATE TABLE reagentes_controlados (
    controlado_id integer not null,
    orgao_controlador text not null
    ato_orgao_controlador text not null,

    FOREIGN KEY (controlado_id) REFERENCES reagentes (reagente_id)
    ON DELETE CASCADE ON UPDATE NO ACTION    
);



CREATE TABLE consumo (
 consumo_id integer primary key autoincrement,
 data_id integer,
 almnto_id integer, 
 FOREIGN KEY (data_id) REFERENCES dias (dia_id)
 ON DELETE CASCADE ON UPDATE NO ACTION,
 
 FOREIGN KEY (almnto_id) REFERENCES alimentos (alimento_id)
 ON DELETE CASCADE ON UPDATE NO ACTION

 );