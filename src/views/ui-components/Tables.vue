<script setup>
import { ref, onMounted } from 'vue';
import UiChildCard from '@/components/shared/UiChildCard.vue';
//import { on } from 'events';
//Modificar para que se pueda conectar a la base de datos user, acceso y correo 
//modificar y colocar botones de editar y eliminar usuarios
const users = ref([]);
const errorMessage = ref(''); // Nombre corregido: errorMessages -> errorMessage

onMounted(async () => {
    try {
        const token = localStorage.getItem('token'); // Obtén el token del localStorage

        const response = await fetch('/api/users', {
            headers: {
                'Authorization': `Bearer ${token}` // Usa el token obtenido
            }
        });

        if (response.ok) {
            users.value = await response.json();
            errorMessage.value = ''; // Limpia el mensaje de error si la petición es exitosa
        } else {
            const errorData = await response.json();
            errorMessage.value = errorData.message || 'Error al obtener usuarios.'; // Usa errorMessage
            console.error('Error:', response.status, response.statusText);
        }
    } catch (error) {
        errorMessage.value = error.message; // Usa errorMessage
        console.error('Error:', error);
    }
});
</script>

<template>

    <div>
    <div v-if="errorMessage">{{ errorMessage }}</div>
    </div>

   <v-row class="month-table">
        <v-col cols="12" sm="12">
            <UiChildCard title="Tabla de usuario">
                <v-table fixed-header height="300px">
                    <thead>
                        <tr>
                            <th class="text-left">Name</th>
                            <th class="text-left">Acceso</th>
                            <th class="text-left">Correo</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="user in users" :key="user.username">
                            <td>{{ user.username }}</td>
                            <td>{{ user.role }}</td>
                            <td>{{ user.email }}</td>
                        </tr>
                    </tbody>
                </v-table>
                <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
             </UiChildCard>
        </v-col>
    </v-row>
</template>