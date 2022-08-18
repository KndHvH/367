```sql

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

db.Alunos.insert({nome:"Carlos",sobrenome:"Antunes",idade:60})
{ acknowledged: true,
  insertedIds: { '0': ObjectId("62f456b25f6499f486a2730a") } }

db.Alunos.insert({nome:"Pedro",sobrenome:"Faria",idade:20})
{ acknowledged: true,
  insertedIds: { '0': ObjectId("62f456c25f6499f486a2730b") } }

db.Alunos.insert({nome:"Marcelo",sobrenome:"Carvalho",idade:30})
{ acknowledged: true,
  insertedIds: { '0': ObjectId("62f456da5f6499f486a2730c") } }

db.Alunos.insert({nome:"Julia",sobrenome:"Pereira",idade:35})
{ acknowledged: true,
  insertedIds: { '0': ObjectId("62f456ef5f6499f486a2730d") } }

db.Alunos.find({idade:{$gt:30}})
{ _id: ObjectId("62f452415f6499f486a27308"),
  nome: 'Joao',
  sobrenome: 'Silva',
  idade: 40 }
{ _id: ObjectId("62f453075f6499f486a27309"),
  nome: 'Maria',
  sobrenome: 'Antunes',
  idade: 55 }
{ _id: ObjectId("62f456b25f6499f486a2730a"),
  nome: 'Carlos',
  sobrenome: 'Antunes',
  idade: 60 }
{ _id: ObjectId("62f456ef5f6499f486a2730d"),
  nome: 'Julia',
  sobrenome: 'Pereira',
  idade: 35 }

db.Alunos.createIndex({"sobrenome":1,"nome":1})
'sobrenome_1_nome_1'

db.Alunos.getIndexes()
[
  { v: 2, key: { _id: 1 }, name: '_id_' },
  { v: 2, key: { sobrenome: 1, nome: 1 }, name: 'sobrenome_1_nome_1' }
]

db.Alunos.dropIndex("sobrenome_1_nome_1")
{ nIndexesWas: 2, ok: 1 

db.Alunos.createIndex({"sobrenome":1,"nome":-1})
'sobrenome_1_nome_-1'

db.Alunos.createIndex({"idade":1})
'idade_1'

db.Alunos.getIndexes()
[
  { v: 2, key: { _id: 1 }, name: '_id_' },
  {
    v: 2,
    key: { sobrenome: 1, nome: -1 },
    name: 'sobrenome_1_nome_-1'
  },
  { v: 2, key: { idade: 1 }, name: 'idade_1' }
]
```