<script setup lang="ts">
import { ref } from "vue";
import ProfitExpanse from "@/components/dashboards/ThumedadTemperatura.vue";
import TrafficDistribution from "@/components/dashboards/Temperatura.vue";
import ProductSales from "@/components/dashboards/THumedad.vue";

// import ProductCards from "@/components/dashboards/ProductCards.vue";
</script>

<template>
    <v-row>
        <v-col cols="12" sm="12" lg="8">
            <ProfitExpanse />
        </v-col>
        <v-col cols="12" sm="12" lg="4">
            <div class="mb-6">
                <TrafficDistribution/>
            </div>
            <div>
                <ProductSales/>
            </div>
        </v-col>

    </v-row>
</template>