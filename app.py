from flask import Flask, render_template, request, redirect, url_for, flash, session
import re

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    codigo = request.form.get('codigo', '').strip()
    
    if not codigo:
        flash('Por favor, digite o código de barras', 'error')
        return redirect(url_for('index'))
    
    # Remove todos os caracteres não numéricos para validação
    codigo_limpo = re.sub(r'[^0-9]', '', codigo)
    
    # Validação básica: deve ter 47 dígitos
    if len(codigo_limpo) != 47:
        flash(f'Código inválido. Digite exatamente 47 números. Você digitou {len(codigo_limpo)} números.', 'error')
        return redirect(url_for('index'))
    
    # Armazena o código formatado na sessão para mostrar na página de sucesso
    session['codigo_formatado'] = codigo
    session['numero_digitados'] = len(codigo_limpo)
    
    return redirect(url_for('success'))

@app.route('/success')
def success():
    codigo_formatado = session.get('codigo_formatado', '')
    numero_digitados = session.get('numero_digitados', 0)
    
    if not codigo_formatado:
        return redirect(url_for('index'))
    
    return render_template('success.html', 
                         codigo_formatado=codigo_formatado,
                         numero_digitados=numero_digitados)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
