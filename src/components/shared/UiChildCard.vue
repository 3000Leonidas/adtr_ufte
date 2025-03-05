<script setup lang="ts">
const props = defineProps({
    title: String
});
</script>
// ===============================|| Ui Child Card ||=============================== //
<!--Table lInk-->
<template>
    <v-card elevation="10" class="bg-surface">
        <v-card-item class="py-4 px-5">
            <v-card-title class="text-h5">{{ title }}</v-card-title>
        </v-card-item>
        <v-divider />
        <v-card-text>
            <slot />
        </v-card-text>
    </v-card>
</template>