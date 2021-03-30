from datetime import datetime, time, timedelta, timezone

formato = '%H:%M:%S'

def relojLocal():
    return datetime.now()

def relojGlobal():
    return datetime.utcnow()

def relojEur():
    eur = timezone(timedelta(hours=+1))
    return datetime.now(eur)

def relojIndia():
    india = timezone(timedelta(hours=+5, minutes=+30))
    return datetime.now(india)

def agregarTiempo(hora, minutos, segundos, reloj):
    suma = timedelta(hours=hora, minutes=minutos, seconds=segundos) 
    return reloj + suma

def quitarTiempo(hora, minutos, segundos, reloj):
    resta = timedelta(hours=hora, minutes=minutos, seconds=segundos)
    return reloj - resta

def imprimirHora(reloj):
    return reloj.strftime(formato)

def cambioHora(hora, minutos, segundos):
    nuevaHora = str(hora) + ':' + str(minutos) + ':' + str(segundos)
    hr = datetime.strptime(nuevaHora, formato)

    return hr