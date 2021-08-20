<template>
  <div id="app">
    <!--
      note: this should use a config variable or something,
      but I'm too lazy right now to figure out how to do that in Vue
     -->
    <NERTagging nerURL="http://localhost:5000/ner" />
  </div>
</template>

<script>
import NERTagging from './components/NERTagging.vue'

export default {
  name: 'App',
  components: {
    NERTagging
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
