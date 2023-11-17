<template>
  <div class="container">
    <div class="card" v-for="envoi in envois" :key="envoi.id" @click="goToCardDetail(envoi.id)">
      <h5 class="">{{ envoi.title }}</h5>
      <p class="">{{ envoi.description }}</p>
    </div>
    <EnvoiComponent />
  </div>
</template>
<script>
export default {
  data() {
    return {
      envois: [
        { id: 1, title: 'Card 1', description: 'Description for Card 1' },
        { id: 2, title: 'Card 2', description: 'Description for Card 2' }
      ]
    }
  },
  methods: {
    goToCardDetail(id) {
      this.$router.push(`/card/${id}`);
    }
  }
}
</script>
