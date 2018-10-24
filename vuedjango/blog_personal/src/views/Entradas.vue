<template>
      <div class="entradas">
    <h1>Hola es una entrada nueva </h1>
     <router-link :to="{name:'entradas-crear'}">Crear nueva entrada</router-link>
    <table>
        <tr>
            <td>ID</td>
            <td>TITULO</td>
            <td>CONTENIDO</td>
            <td>AUTOR</td>
            <td>OPCIONES</td>
        </tr>
        <tr v-for="entrada in entradas"> 
            <td>{{entrada.id}}</td>
            <td>{{entrada.titulo}}</td>
            <td>{{entrada.contenido}}</td>
            <td>{{entrada.nombreAutor}}</td>
            <td>
            <router-link :to="{name:'entradas-editar',params:{id:entrada.id}}">EDITAR</router-link> |
                <a @click.prevent="EliminarEntrada(entrada.id)" href="#">Eliminar</a>
            </td>
        </tr>
    </table>      
  </div>
</template>

<script>

import axios from 'axios'

export default {
    mounted(){
        this.CargarEntradas()
    },
    data(){
        return{
            entradas:[]
        }
    },
     methods: {
         CargarEntradas(){
            var self = this;
            axios.get('http://127.0.0.1:8000/api/entradas/')
            .then(function(response){
            self.entradas = response.data
        });  
         },
         EliminarEntrada(id){
             let op = window.confirm("Esta seguro de eliminar la entrada")
             if(op){
                axios.delete('http://127.0.0.1:8000/api/entradas/'+id+'/')
                .then(respuesta =>{
                 console.log(respuesta)
                 this.CargarEntradas()
             })
             }


         }
     }
}

</script>

<style>

table{
    margin: 0 auto;
    border: 5px
}


</style>
