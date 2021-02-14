<template>
  <div class="container">
    <div class="main">
      <div class="logo">
        <img src="./assets/logo.png" alt="Blue Pages Logo">
      </div>
      <div class="form-and-results">
        <div class="form">
          <div class="form-title">
            <div class="title">Blue Pages helps you find anyone in seconds!</div>
            <div class="subtitle">Enter the fields below</div>
          </div>
          <div class="input-fields">
            <input v-model="firstName" type="text" placeholder="FIRST NAME">
            <input v-model="lastName" type="text" placeholder="FIRST NAME">
            <select v-model="state">
              <option value="">State</option>
              <option v-for="state in states" :value="state.abbreviation">{{ state.name }}</option>
            </select>
            <button @click="search">Search</button>
          </div>
        </div>
        <div class="results-container">
          <div class="results-title">Results</div>
          <div class="results">
            <div class="result" v-for="result in results">
              <div class="result-col">
                <div class="result-col-title">
                  FIRST NAME
                </div>
                <div class="result-col-val">
                  {{ result.first_name }}
                </div>
              </div>
              <div class="result-col">
                <div class="result-col-title">
                  LAST NAME
                </div>
                <div class="result-col-val">
                  {{ result.last_name }}
                </div>
              </div>
              <div class="result-col">
                <div class="result-col-title">
                  STATE
                </div>
                <div class="result-col-val">
                  {{ result.state }}
                </div>
              </div>
              <div class="result-col">
                <div class="result-col-title">
                  PHONENUMBER
                </div>
                <div class="result-col-val">
                  {{ result.phonenumber }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

const API_URL = "http://localhost:8080";

export default {
  name: 'App',
  components: {},

  data() {
    return {
      firstName: "",
      lastName: "",
      state: "",
      states: [
        {"name":"Alabama","abbreviation":"AL"},
        {"name":"Alaska","abbreviation":"AK"},
        {"name":"Arizona","abbreviation":"AZ"},
        {"name":"Arkansas","abbreviation":"AR"},
        {"name":"California","abbreviation":"CA"},
        {"name":"Colorado","abbreviation":"CO"},
        {"name":"Connecticut","abbreviation":"CT"},
        {"name":"Delaware","abbreviation":"DE"},
        {"name":"District of Columbia","abbreviation":"DC"},
        {"name":"Florida","abbreviation":"FL"},
        {"name":"Georgia","abbreviation":"GA"},
        {"name":"Hawaii","abbreviation":"HI"},
        {"name":"Idaho","abbreviation":"ID"},
        {"name":"Illinois","abbreviation":"IL"},
        {"name":"Indiana","abbreviation":"IN"},
        {"name":"Iowa","abbreviation":"IA"},
        {"name":"Kansa","abbreviation":"KS"},
        {"name":"Kentucky","abbreviation":"KY"},
        {"name":"Lousiana","abbreviation":"LA"},
        {"name":"Maine","abbreviation":"ME"},
        {"name":"Maryland","abbreviation":"MD"},
        {"name":"Massachusetts","abbreviation":"MA"},
        {"name":"Michigan","abbreviation":"MI"},
        {"name":"Minnesota","abbreviation":"MN"},
        {"name":"Mississippi","abbreviation":"MS"},
        {"name":"Missouri","abbreviation":"MO"},
        {"name":"Montana","abbreviation":"MT"},
        {"name":"Nebraska","abbreviation":"NE"},
        {"name":"Nevada","abbreviation":"NV"},
        {"name":"New Hampshire","abbreviation":"NH"},
        {"name":"New Jersey","abbreviation":"NJ"},
        {"name":"New Mexico","abbreviation":"NM"},
        {"name":"New York","abbreviation":"NY"},
        {"name":"North Carolina","abbreviation":"NC"},
        {"name":"North Dakota","abbreviation":"ND"},
        {"name":"Ohio","abbreviation":"OH"},
        {"name":"Oklahoma","abbreviation":"OK"},
        {"name":"Oregon","abbreviation":"OR"},
        {"name":"Pennsylvania","abbreviation":"PA"},
        {"name":"Rhode Island","abbreviation":"RI"},
        {"name":"South Carolina","abbreviation":"SC"},
        {"name":"South Dakota","abbreviation":"SD"},
        {"name":"Tennessee","abbreviation":"TN"},
        {"name":"Texas","abbreviation":"TX"},
        {"name":"Utah","abbreviation":"UT"},
        {"name":"Vermont","abbreviation":"VT"},
        {"name":"Virginia","abbreviation":"VA"},
        {"name":"Washington","abbreviation":"WA"},
        {"name":"West Virginia","abbreviation":"WV"},
        {"name":"Wisconsin","abbreviation":"WI"},
        {"name":"Wyoming","abbreviation":"WY"}
      ],

      results: [],
    };
  },

  methods: {
    async search() {
      const searchParams = {
        firstName: this.firstName,
        lastName: this.lastName,
        state: this.state
      };

      const queryParams = new URLSearchParams(searchParams).toString();

      const request = await fetch(`${API_URL}/search/?${queryParams}`);

      if (!request.ok) {
        alert("Something went wrong while fetching the results");
        return;
      }

      this.results = await request.json();
    },
  }
}
</script>

<style>
html, body { 
  --dark-blue: #3E6697;
  --light-blue: #E9F3FF;
  margin: 0; 
  padding: 0; 
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 100%;
  height: 100%;
  color: var(--dark-blue);
  background-color: var(--light-blue);
}

.container {
  height: 100%;
  width: 100%;
}

.logo img {
  width: 200px;
}

.main {
  padding: 1rem 3rem;
}

.form-and-results {
  margin-top: 3%;
}

.form-title .title {
  font-weight: bold;
  font-size: 1rem;
}

.form-title .subtitle {
  font-size: 0.8rem;
  margin-top: 1rem;
}

.form .input-fields {
  margin-top: 1rem;
  margin-bottom: 1rem;
  display: flex;
  flex-direction: column;
}

.input-fields > * {
  margin-top: 1rem;
}

.results > * {
  margin-top: 1rem;
}

.result {
  display: flex;
  flex-direction: row;
  justify-content: space-between; 
}
</style>
