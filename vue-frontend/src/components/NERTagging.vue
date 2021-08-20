<template>
  <div class="hello">
    <h1>Joe's named entity getter app</h1>
    <form>
        <textarea id="input-text" name="text" v-model="text">
            The pilot, John Doe, flew over the United States in his airplane.
        </textarea>
        <br>
        <input type="button" value="Go" v-on:click="tagText" />
        <br>

        <output>
            <ul>
                <li v-for="entity in entities" v-bind:key="entity.name">
                    <span class="entity-name">{{ entity.name }}</span>:
                    <span class="entity-type">{{ entity.type }}</span>
                </li>
            </ul>
        </output>
    </form>
  </div>
</template>

<script>
export default {
  name: 'NERTagging',
  data: function () {
    return {
      "text": "The pilot, John Doe, flew over the United States in his airplane.",
      "entities": [
        {"name": "John Doe", "type": "PERSON"},
        {"name": "United States", "type": "GPE"},
      ],
      "entities-alt": {"John Doe": "PERSON", "United States": "GPE"},
    }
  },
  methods: {
     tagText: function () {
        console.log(this.text)
     }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
textarea#input-text {
    width: 50em;
    height: 30em;
}

span.entity-type {
    color: red;
}

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
