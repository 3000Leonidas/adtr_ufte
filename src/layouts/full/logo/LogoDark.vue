<script setup lang="ts">
import { RouterLink } from 'vue-router';
import logo from '@/assets/images/logos/ibmetro.jpg';
</script>
<template>
    <div class="logo">
        <RouterLink to="/">
            <img :src="logo" alt="home" style="width: 250px;" />
        </RouterLink>
    </div>
</template>
