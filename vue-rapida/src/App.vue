<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/envois">Envois</router-link> |
    <router-link to="/about">About</router-link>
  </nav>
  <div class="container">
    <router-view />
  </div>
</template>

<style lang="scss">
//I can redifine bootstrap scss variables when using boostrap since I will import it as below
$primary: #6f42c1;
@import 'node_modules/bootstrap/scss/bootstrap';
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
