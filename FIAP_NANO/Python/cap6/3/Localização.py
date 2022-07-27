from pygeocoder import Geocoder

endereço = "650, Luiz dos santos cabral 650, são paulo, SP"

print(Geocoder("CODIGO DA API").geocode(endereço).coordinates)

#Api é paga, mas deve dar as coordenadas do endereço