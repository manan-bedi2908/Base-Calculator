from flask import Flask, render_template, request
app = Flask(__name__)

def getProductWithSingleDigit(base, n1, d2):
    rv = 0
    p = 1
    c = 0
    while (n1 > 0 or c > 0):
        d1 = int(n1 % 10)
        n1 //= 10
        d = int(d1 * d2 + c)
        c = d // base
        d = int(d % base)
        rv = rv + d * p
        p *= 10
    return rv

def getSum(base, n1, n2) :
        rv = 0
        p = 1
        c = 0
        while (n1 > 0 or n2 > 0 or c > 0):
            d1 = int(n1 % 10)
            d2 = int(n2 % 10)
            n1 //= 10
            n2 //= 10
            d = d1 + d2 + c
            c = d // base
            d = int(d % base)
            rv += d * p
            p *= 10
        return rv

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/base_convertor', methods=['GET','POST'])
def base_convertor():
    if request.method == 'POST':
        n = int(request.form['number'])
        from_base = int(request.form['choice_1'])
        to_base = int(request.form['choice_2'])
        rv = 0;
        p = 1;
        on = n
        while (n > 0):
            dig = int(n % 10)
            rv = int(rv + dig*p)
            p *= from_base
            n = n // 10
        res = 0
        po = 1
        while (rv > 0):
            rem = int(rv % to_base)
            rv = rv // to_base
            res += rem * po
            po *= 10
    return render_template('index.html', res = res, n=on, from_base=from_base, to_base=to_base)

@app.route('/base_calculator', methods=['GET','POST'])
def base_calculator():
    if request.method == 'POST':
        base = int(request.form['base'])
        n1 = int(request.form['first_number'])
        n2 = int(request.form['second_number'])
        op = request.form['op']
        on1 = n1
        on2 = n2
        if op == '+':
            rv = 0
            p = 1
            c = 0
            while (n1 > 0 or n2 > 0 or c > 0):
                d1 = int(n1 % 10)
                d2 = int(n2 % 10)
                n1 //= 10
                n2 //= 10
                d = d1 + d2 + c
                c = d // base
                d = int(d % base)
                rv += (d * p)
                p *= 10

        elif op == '-':
            rv = 0
            p = 1
            c = 0
            if (n1 > n2):
                temp = n1
                n1 = n2
                n2 = temp

            while (n2 > 0):
                d1 = int(n1 % 10)
                d2 = int(n2 % 10)
                n1 //= 10
                n2 //= 10
                d = 0
                d2 = d2 + c
                if (d2 >= d1):
                    c = 0
                    d = d1 - d2
                else:
                    c = -1
                    d = d2 + base - d1
                rv += d * p
                p *= 10
        else:
            rv = 0
            p = 1
            while (n2 > 0):
                d2 = int(n2 % 10)
                n2 //= 10
                single_product = getProductWithSingleDigit(base, n1, d2)
                single_product *= p;
                rv = getSum(base, rv, single_product);
                p *= 10;

    return render_template('index.html', res = rv, base=base, n1=on1, n2=on2, op=op)


if __name__ == '__main__':
    app.run(debug=True)

