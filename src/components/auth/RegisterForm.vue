<script setup lang="ts">
import { ref } from 'vue';
const checkbox = ref(false);

const username = ref('');
const email = ref('');
const password = ref('');
const errorMessage = ref('');
const successMessage = ref('');

const register = async () => {
    errorMessage.value = '';
    successMessage.value = '';

    if (!username.value || !email.value || !password.value) {
        errorMessage.value = 'Usuario, email y contraseña son requeridos';
        return;
    }

    try {
        const response = await fetch('/api/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username.value,
                // email: email.value,  // Si tu backend no usa el email, puedes quitar esta línea
                password: password.value
            })
        });

        if (response.ok) {
            successMessage.value = 'Usuario registrado exitosamente.';
            username.value = ''; // Limpiar los campos después del registro
            email.value = '';
            password.value = '';
            
        } else if (response.status === 400) {
            const errorData = await response.json();
            errorMessage.value = errorData.message || 'Error al registrar usuario.';
        } else {
            errorMessage.value = 'Error al registrar usuario. Inténtalo de nuevo más tarde.';
            console.error('Error en la solicitud:', response.status, response.statusText);
        }
    } catch (error) {
        errorMessage.value = 'Error al registrar usuario. Inténtalo de nuevo más tarde.';
        console.error('Error:', error);
    }
};

</script>
<template>
 <div >
    <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
    <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
     <v-row class="d-flex  mb-3">
         <v-col cols="12">
             <v-label class="font-weight-medium mb-1">Usuario</v-label>
             <v-text-field v-model="username" variant="outlined" hide-details color="primary"></v-text-field>
            </v-col>
            <v-col cols="12">
                <v-label class="font-weight-medium mb-1">Correo Electronico</v-label>
                <v-text-field v-model="email" variant="outlined" type="email" hide-details color="primary"></v-text-field>
            </v-col>
            <v-col cols="12">
                <v-label class="font-weight-medium mb-1">Contraseña</v-label>
                <v-text-field v-model="password" variant="outlined" type="password"  hide-details color="primary"></v-text-field>
            </v-col>
            <v-col cols="12">
                <v-btn @click="register" color="primary" rounded="pill" size="large" block flat>Sign up</v-btn>
            </v-col>
        </v-row>
    </div>
</template>
