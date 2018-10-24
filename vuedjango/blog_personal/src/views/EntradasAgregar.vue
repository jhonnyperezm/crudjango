<template>
    <div class="entradas-crear">
        <h1 v-if="entrada.id!=null">Pagina de Editar </h1>    
        <h1 v-else>Pagina de Agregar </h1>    
        <form action="">
            <label for="">Titulo</label>
            <input type="text" v-model="entrada.titulo"><br>
            <label for="">Contenido</label>
            <textarea name="" id="" cols="30" rows="10" v-model="entrada.contenido"></textarea><br>
            <label for="">autor</label>
            <select name="" id="" v-model="entrada.autor">
                <option v-for="autor in autores" :value="autor.id" >{{autor.nombre}}-{{autor.documento}}</option>
            </select>
            <br>
            <button v-if="entrada.id!=null" @click.prevent="GuardarEntrada" type="button" name="button">Editar entrada</button>
            <button v-else @click.prevent="GuardarEntrada" type="button" name="button">Crear entrada</button>
        </form>    
    </div>
</template>

<script>

import axios from 'axios'

export default {
    name:'entradas-crear',
    mounted(){
        var self = this;
        let id= this.$route.params.id

        if(id!=null){
            axios.get('http://127.0.0.1:8000/api/entradas/'+id)
            .then(function(response){
            self.entrada = response.data
            })
        }
        axios.get('http://127.0.0.1:8000/api/autores/')
        .then(function(response){
        self.autores = response.data
        })
    },
    data(){
        return{
            autores:[],
            entrada:{id:null,titulo:'',contenido:'',autor:null}
        }
    },
    methods:{
        GuardarEntrada(){
            var datos={
                titulo:this.entrada.titulo,
                contenido:this.entrada.contenido,
                autor:this.entrada.autor
            }

            let router = this.$router

            if(this.entrada.id!=null){
                axios.put('http://127.0.0.1:8000/api/entradas/'+this.entrada.id +'/',datos)
                .then(response =>{
                    if(response.statusText=="OK"){
                        router.push('/Entradas')
                    }else{
                        console.log("error"+response.data)
                        alert("error al crear ")
                    }
                })

            }else{
                axios.post('http://127.0.0.1:8000/api/entradas/', datos)
                .then(response => { 
                    if(response.statusText == "Created"){
                        router.push('/Entradas')
                    }else{
                        console.log("error"+response.data)
                        alert("error al crear ")
                    }
                });
            }
        }
    }

}
</script>

<style>

</style>
