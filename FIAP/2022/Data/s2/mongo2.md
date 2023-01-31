```sql
db.getCollection("alunos").aggregate([{"$lookup":{ from: "checkpoints", localField:"matricula", foreignField:"matricula", as:"nota"}}]);
{ _id: ObjectId("62fd8f7d8b688e2e55012271"),
  nome: 'João',
  sobrenome: 'Silva',
  idade: 40,
  matricula: 1,
  nota: 
   [ { _id: ObjectId("62fd8b648b688e2e55012264"),
       matricula: 1,
       checkpoint: 1,
       disciplina: 'Cognitive Data Science',
       nota: 10 },
     { _id: ObjectId("62fd8b648b688e2e55012265"),
       matricula: 1,
       checkpoint: 2,
       disciplina: 'Cognitive Data Science',
       nota: 5 },
     { _id: ObjectId("62fd8b648b688e2e55012266"),
       matricula: 1,
       checkpoint: 3,
       disciplina: 'Cognitive Data Science',
       nota: 8 } ] }
{ _id: ObjectId("62fd8f7d8b688e2e55012272"),
  nome: 'José Luís',
  sobrenome: 'Santos',
  idade: 35,
  matricula: 2,
  nota: 
   [ { _id: ObjectId("62fd8b648b688e2e55012267"),
       matricula: 2,
       checkpoint: 1,
       disciplina: 'Cognitive Data Science',
       nota: 4 },
     { _id: ObjectId("62fd8b648b688e2e55012268"),
       matricula: 2,
       checkpoint: 2,
       disciplina: 'Cognitive Data Science',
       nota: 9 },
     { _id: ObjectId("62fd8b648b688e2e55012269"),
       matricula: 2,
       checkpoint: 3,
       disciplina: 'Cognitive Data Science',
       nota: 7 } ] }
{ _id: ObjectId("62fd8f7d8b688e2e55012273"),
  nome: 'Antônio',
  sobrenome: 'Silva',
  idade: 42,
  matricula: 3,
  nota: 
   [ { _id: ObjectId("62fd8b648b688e2e5501226a"),
       matricula: 3,
       checkpoint: 1,
       disciplina: 'Cognitive Data Science',
       nota: 6 },
     { _id: ObjectId("62fd8b648b688e2e5501226b"),
       matricula: 3,
       checkpoint: 2,
       disciplina: 'Cognitive Data Science',
       nota: 7 },
     { _id: ObjectId("62fd8b648b688e2e5501226c"),
       matricula: 3,
       checkpoint: 3,
       disciplina: 'Cognitive Data Science',
       nota: 10 } ] }
{ _id: ObjectId("62fd8f7d8b688e2e55012274"),
  nome: 'Alice',
  sobrenome: 'Silva',
  idade: 40,
  matricula: 4,
  nota: [] }
{ _id: ObjectId("62fd8f7d8b688e2e55012275"),
  nome: 'Rita',
  sobrenome: 'Santos',
  idade: 43,
  matricula: 5,
  nota: [] }
db.alunos.aggregate([{$group:{_id:"$matricula",soma_notas:{$sum:"$nota"}}}])
{ _id: 2, soma_notas: 0 }
{ _id: 1, soma_notas: 0 }
{ _id: 3, soma_notas: 0 }
{ _id: 4, soma_notas: 0 }
{ _id: 5, soma_notas: 0 }
db.checkpoints.aggregate([{$group:{_id:"$matricula",soma_notas:{$sum:"$nota"}}}])
{ _id: 1, soma_notas: 23 }
{ _id: 2, soma_notas: 20 }
{ _id: 3, soma_notas: 23 }
db.checkpoints.aggregate([{$group:{_id:"$matricula",soma_notas:{$max:"$nota"}}}])
{ _id: 1, soma_notas: 10 }
{ _id: 2, soma_notas: 9 }
{ _id: 3, soma_notas: 10 }
db.checkpoints.aggregate([{$group:{_id:"$matricula",soma_notas:{$mmin:"$nota"}}}])
MongoServerError: unknown group operator '$mmin'
db.checkpoints.aggregate([{$group:{_id:"$matricula",soma_notas:{$min:"$nota"}}}])
{ _id: 3, soma_notas: 6 }
{ _id: 2, soma_notas: 4 }
{ _id: 1, soma_notas: 5 }
```
