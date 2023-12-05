const express = require('express')
const app = express()

app.get('/', (req, res) => {
  res.send('Main Page')
})
app.get('/tosbaga', (req,res) => {
  res.send("tosbaga");
});
app.get('/skeleton', (req,res) => {
  res.send("skeleton");
});
app.post('/', (req, res) => {
  res.send('Got a POST request')
})
app.put('/user', (req, res) => {
  res.send('Got a PUT request at /user')
})
app.delete('/user', (req, res) => {
  res.send('Got a DELETE request at /user')
})
app.all('/secret', (req, res, next) => {
  console.log('Accessing the secret section ...')
  next() 
})
app.get('/', (req, res) => {
  res.send('root')
})
app.get('/about', (req, res) => {
  res.send('about')
})
app.get('/a.html', (req, res) => {
  res.send("a.html")
})
app.listen(4000, ()=>{
  console.log("listening to port 4000");
});