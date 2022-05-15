const app = Vue.createApp({
    data() {
        return {
            Name: '',
            Type: '',
            picture: ''
        }
    },
    methods: {
        async getUser() {
            
            const res = await fetch('https://southcentralus.api.cognitive.microsoft.com/');//Conexion a API
            const { results } = await res.json();
            
            this.Name = Name
            this.Type = Type
            this.picture = picture
        },  
    }
})

app.mount('#app');