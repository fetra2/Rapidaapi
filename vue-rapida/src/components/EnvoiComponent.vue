<template>
  <p>grr</p>
</template>
<script>
export default {
  data() {
    return {
      envois: [
        { id: 1, title: 'Card 1', description: 'Description for Card 1' },
        { id: 2, title: 'Card 2', description: ' Description for Card 2' }
      ]
    }
  },
  methods: {
    goToCardDetail(id) {
      this.$router.push(`/card/${id}`)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.card {
  cursor: pointer;
  margin: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
</style>
