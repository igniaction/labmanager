from flask import Flask, render_template, url_for, request
from database import get_db
from molmass import Formula

f = Formula('C8H10N4O2')

print(f'Fórmula: {f.formula}')
print(f'Massa: {f.mass}')




app = Flask(__name__)


users = {
        'login': 'elaine.aquino', 
        'senha':'142753'
        }



########################################
@app.route('/', methods=['GET', 'POST'])
def index():

    
    
    print(f"User: {users['login']}")
    print(f"Senha: {users['senha']}")

    return render_template('base.html')







########################################
@app.route('/reagentes', methods=['GET', 'POST'])
def reagentes():
    return render_template('reagentes.html')




########################################
@app.route('/cas', methods=['GET','POST'])
def cas():
    return render_template('cas.html')







########################################
@app.route('/consulta/cas', methods=['GET', 'POST'])
def consulta_cas():
    db = get_db()
    cas_results=''
    if request.method == 'POST':
        cas = request.form['numero_cas']
        cas_cur = db.execute('select * from chemical_abstract_service where numero_cas = ?', [cas])
        cas_results = cas_cur.fetchone()

    return render_template('consultacas.html', cas_results=cas_results)

########################################
@app.route('/atualiza/cas', methods=['GET', 'POST'])
def atualiza_cas():
    user = request.args.get('login')
    psswd = request.args.get('senha')
    db = get_db()
    cas_results=''
    if request.method == 'POST':
        cas = request.form['numero_cas']
        cas_cur = db.execute('select * from chemical_abstract_service where numero_cas = ?', [cas])
        cas_results = cas_cur.fetchone()
        id = cas_results['element_id']
        
        if request.form['option'] == 'Atualiza':
            formula = request.form['formula']
            nome = request.form['nomenclatura']
            n_cas = request.form['numero_cas']       
            db.execute('''update chemical_abstract_service
                      set formula = ?, 
                      nomenclatura = ?, 
                      numero_cas = ?
                      where element_id = ?''', [formula, nome, n_cas, id])
            db.commit()   
        
            print(f"F: {request.form['formula']}")
            print(f"N: {request.form['nomenclatura']}")
            print(f"C: {request.form['numero_cas']}")       
     
    return render_template('atualizacas.html', cas_results=cas_results)
    

########################################
@app.route('/registra/cas', methods=['GET', 'POST'])
def registra_cas():
    cas_results=''

    db = get_db()
    if request.method == 'POST':
        formula = request.form['formula']
        nome = request.form['nomenclatura']
        n_cas = request.form['numero_cas']
        db.execute('''insert into chemical_abstract_service (formula, nomenclatura, numero_cas)
                      values (?, ?, ?)''', [formula, nome, n_cas])
        db.commit()
    cas_cur = db.execute('select * from chemical_abstract_service order by nomenclatura ASC')
    cas_results = cas_cur.fetchall()

    return render_template('registracas.html', cas_results=cas_results)

########################################
if __name__ == '__main__':
    app.run(debug=True)