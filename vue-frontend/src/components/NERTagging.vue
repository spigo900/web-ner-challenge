<template>
  <div class="hello">
    <h1>Joe's named entity getter app</h1>
    <form id="input-form">
        <textarea id="input-text" name="text" v-model="text"></textarea>
        <br>
        <input type="button" value="Go" v-on:click="onGo" />
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
  props: ['nerURL'],
  data: function () {
    var text = "The pilot, John Doe, flew over the United States in his airplane.";
    return {
      "text": text,
      "entities": this.tagText(text),
    }
  },
  methods: {
     onGo: function () {
        this.tagText(this.text);
     },
     tagText: function (text) {
        var component = this;
        function receiveTags() {
            component.entities = request.response.ner;
        }

        var request = new XMLHttpRequest();
        request.responseType = "json"
        request.open("POST", this.nerURL);
        request.onload = receiveTags;
        var formData = new FormData();
        formData.append("text", text);
        request.send(formData);
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
