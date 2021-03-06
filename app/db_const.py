import os

HOSTNAME = 'localhost'
DATABASE = 'snp_index'
USERNAME = os.environ.get('DB_USER', 'onmaisiadmin')
PASSWORD = os.environ.get('DB_PASSWD', 'onmaisiadmin')
DB_URI = 'mysql://{}:{}@{}/{}'.format(
    USERNAME, PASSWORD, HOSTNAME, DATABASE)

get_head_cmd = """
    select column_name from information_schema.columns
    where table_schema='snp_index' and table_name='{}';
    """
get_unique_cmd = "select distinct() from {};"

create_expr_cmd = """
                  create table {}(Id INT PRIMARY KEY AUTO_INCREMENT,
                                  GENE_ID VARCHAR(20),
                                  CHR VARCHAR(5),
                                  POS_START VARCHAR(50),
                                  POS_END VARCHAR(50),
                  """


create_snp_cmd = """
                   create table {}(Id INT PRIMARY KEY AUTO_INCREMENT,
                                   CHR VARCHAR(5),
                                   POS VARCHAR(50),
                                   REF VARCHAR(10),
                                   ALT VARCHAR(10),
                                   FEATURE VARCHAR(50),
                                   GENE VARCHAR(100),
                                   ALLE VARCHAR(20),
                   """

create_locus_cmd = """
                    create table {}(Id INT PRIMARY KEY AUTO_INCREMENT,
                                    GENE_ID VARCHAR(20),
                                    CHR VARCHAR(5),
                                    POS_START VARCHAR(50),
                                    POS_END VARCHAR(50)                               
"""

create_func_cmd = """
                    create table {}(Id INT PRIMARY KEY AUTO_INCREMENT,
                                    GENE_ID VARCHAR(20),
                                    BLAST_Hit_Accession VARCHAR(200),
                                    Description VARCHAR(200),
                                    Pfam_ID LONGTEXT,
                                    Interpro_ID LONGTEXT,
                                    GO_ID LONGTEXT
"""
create_group_cmd = """
                   create table {}(Id INT PRIMARY KEY AUTO_INCREMENT,
                                   SAMPLE VARCHAR(20),
                                   DESCRIPTION VARCHAR(100),
                   """
create_genetrans_map_cmd = """
                   create table {}(Id INT PRIMARY KEY AUTO_INCREMENT,
                                   GENE_TRANS VARCHAR(100),
                                   GENE VARCHAR(100)
"""
snp_table_info = {'cmd': create_snp_cmd,
                  'fixed_column_num': 7,
                  'fixed_column_name': ('CHR', 'POS', 'REF', 'ALT', 'FEATURE', 'GENE', 'ALLE'),
                  'add_key_str': ',key chrindex (CHR), key posindex (POS)'}

expr_table_info = {'cmd': create_expr_cmd,
                   'fixed_column_num': 4,
                   'fixed_column_name': ('GENE_ID', 'CHR', 'POS_START', 'POS_END'),
                   'add_key_str': ',key geneindex (GENE_ID)'}

locus_table_info = {'cmd': create_locus_cmd,
                    'header': ('GENE_ID', 'CHR', 'POS_START', 'POS_END'),
                    'add_key_str': ',key geneindex (GENE_ID)'}

func_table_info = {'cmd': create_func_cmd,
                   'header': ('GENE_ID', 'BLAST_Hit_Accession', 'Description',
                              'Pfam_ID', 'Interpro_ID', 'GO_ID'),
                   'add_key_str': ',key geneindex (GENE_ID)'}

genetrans_map_info = {'cmd':create_genetrans_map_cmd,
                      'header': ('GENE_TRANS', 'GENE'),
                      'add_key_str': ',key geneindex (GENE_TRANS)'}

table_info = {'snp': snp_table_info,
              'expr': expr_table_info,
              'func': func_table_info,
              'locus': locus_table_info,
              'geneTrans_map': genetrans_map_info}
