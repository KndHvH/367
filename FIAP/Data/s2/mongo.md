```mongodb

show databases
admin   40.00 KiB
config  72.00 KiB
local   40.00 KiB

use outrabase
'switched to db outrabase'

db.createCollection("Alunos")
{ ok: 1 }

show collections
Alunos

db.Alunos.insert({nome:"Joao",sobrenome:"Silva",idade:40})
'DeprecationWarning: Collection.insert() is deprecated. Use insertOne, insertMany, or bulkWrite.'
{ acknowledged: true,
  insertedIds: { '0': ObjectId("62f452415f6499f486a27308") } }
  
db.Alunos.insert({nome:"Maria",sobrenome:"Antunes",idade:55})
{ acknowledged: true,
  insertedIds: { '0': ObjectId("62f453075f6499f486a27309") } }

db.Alunos.find()
{ _id: ObjectId("62f452415f6499f486a27308"),
  nome: 'Joao',
  sobrenome: 'Silva',
  idade: 40 }
{ _id: ObjectId("62f453075f6499f486a27309"),
  nome: 'Maria',
  sobrenome: 'Antunes',
  idade: 55 }

db.Alunos.find({"idade":40})
{ _id: ObjectId("62f452415f6499f486a27308"),
  nome: 'Joao',
  sobrenome: 'Silva',
  idade: 40 }
  
db.Alunos.find({"nome":"Maria"})
{ _id: ObjectId("62f453075f6499f486a27309"),
  nome: 'Maria',
  sobrenome: 'Antunes',
  idade: 55 }

```