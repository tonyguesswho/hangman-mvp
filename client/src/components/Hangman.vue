<template>
  <div>
  <div v-if="loading"> Loading ....</div>
  <div class="container-fluid" v-else>
    <navbar></navbar>
    <b-alert
      variant="danger"
      @dismissed="dismissCountDown=0"
      @dismiss-count-down="countDownChanged"
      v-if="errorMessage"
      dismissible
      :show="dismissCountDown">{{ errorMessage }}
  </b-alert>
    <div class="row d-flex justify-content-center mt-5">
      <b-dropdown text="Select Category" variant="info" class="m-2 col" menu-class="w-100">
        <b-dropdown-item href="#"
          v-for="category in categories" :key="category.id"
          @click="selectCategory(category)">{{category.name}}
        </b-dropdown-item>
      </b-dropdown>
         <div class="col-2 m-2">
         <b-button squared variant="info" v-b-modal.category-modal>Add category</b-button>
      </div>
      <div class="col-4 m-2">
        <span
          v-if="category.description"
          class="text-center text-wrap text-capitalize font-weight-bold text-monospace">
          {{category.description}}
        </span>
        <span
          v-else
          class="text-center text-wrap text-capitalize font-weight-bold text-monospace">
          {{category.name}}
        </span>
      </div>
      <div class="col-2 m-2">
         <b-button squared variant="info" @click="startGame(category)" >Start Game</b-button>
      </div>
    </div>
    <div>
      <alert v-if="lost" :message="message.msg" :variant="message.variant"></alert>
      <alert v-if="won" :message="message.msg" :variant="message.variant"></alert>
    </div>
    <div class="container mt-5 d-flex justify-content-center">
        <div class="letter" v-for="letter in displayLetters " :key="letter">
          {{letter}}
        </div>
    </div>
    <div class="contianer d-flex justify-content-center mt-5">
      <b-button
        :disabled="letter in clicked"
        variant="outline-primary"
        class="mr-2"
        v-for="letter in letters"
        :key=letter
        @click="checkLetter(letter)">
        {{letter}}
        </b-button>
    </div>
      <div class="contianer d-flex justify-content-center mt-5">
      <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="350px" height="260px" viewBox="0 0 350 275"
      preserveAspectRatio="xMidYMid meet">
      <line v-if="strikes > 0"
        x1="80"
        y1="257"
        x2="260" y2="257" style="stroke:black;fill:none;stroke-width:2px;" />
      <line v-if="strikes > 1"
        x1="100"
        y1="257"
        x2="100" y2="40" style="stroke:black;fill:none;stroke-width:2px;" />
      <line v-if="strikes > 2"
        x1="100"
        y1="40"
        x2="230" y2="40" style="stroke:black;fill:none;stroke-width:2px;" />
      <line v-if="strikes > 3"
        x1="100"
        y1="80"
        x2="130" y2="40" style="stroke:black;fill:none;stroke-width:2px;" />
      <line v-if="strikes > 4"
        x1="230"
        y1="40"
        x2="230" y2="80" style="stroke:black;fill:none;stroke-width:2px;" />
      <circle v-if="strikes > 5"
        cx="230" cy="90" style="fill:khaki;stroke:black;stroke-width:2px;" r="20" />
      <line v-if="strikes > 6"
        x1="230"
        y1="110"
        x2="230" y2="170" style="stroke:black;fill:none;stroke-width:2px;" />
      <line v-if="strikes > 7"
        x1="230"
        y1="140"
        x2="250" y2="120" style="stroke:black;fill:none;stroke-width:2px;" />
      <line v-if="strikes > 8"
        x1="230"
        y1="140"
        x2="210" y2="120" style="stroke:black;fill:none;stroke-width:2px;" />
      <line v-if="strikes > 9"
        x1="230"
        y1="170"
        x2="250" y2="200" style="stroke:black;fill:none;stroke-width:2px;" />
      <line v-if="strikes > 10"
        x1="230"
        y1="170"
        x2="210" y2="200" style="stroke:black;fill:none;stroke-width:2px;" />
    </svg>
      </div>
    <b-modal ref="addCategoryModal" id="category-modal" title="Add a new category" hide-footer>
      <b-form class="w-100" @submit="onSubmit">
        <b-form-group
          id="form-category-group"
          label="Category:" label-for="form-category-input">
          <b-form-input
            id="form-category-input"
            type="text"
            v-model="addCategoryForm.category" required placeholder="Enter Category"></b-form-input>
        </b-form-group>
        <b-form-group
          id="form-description-group"
          label="Description:" label-for="form-description-input">
          <b-form-input
            id="form-description-input"
            type="text"
            v-model="addCategoryForm.description"
            placeholder="Enter description"></b-form-input>
        </b-form-group>
        <b-form-group id="form-words-group" label="Words:" label-for="form-words-input">
          <b-form-textarea
          id="form-words-input"
          v-model="addCategoryForm.words"
          placeholder="Enter comma separated words..."></b-form-textarea>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
      </b-form>
    </b-modal>
  </div>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';
import Navbar from './Navbar.vue';

const API_URL = process.env.VUE_APP_API_URL;

export default {
  data() {
    return {
      categories: [],
      dismissSecs: 5,
      dismissCountDown: 0,
      loading: false,
      letters: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
      category: {
        name: '',
        description: '',
      },
      selectedCategory: false,
      addCategoryForm: {
        category: '',
        description: '',
        words: '',
      },
      strikes: 0,
      correct: 0,
      won: false,
      lost: false,
      word: '',
      errorMessage: '',
      displayLetters: [],
      wordLetters: [],
      clicked: [],
      message: {
        msg: '',
        variant: '',
      },
      showMessage: false,
      startedGame: false,
    };
  },
  components: {
    alert: Alert,
    navbar: Navbar,
  },
  methods: {
    async getCategories() {
      this.loading = true;
      const path = `${API_URL}/category`;
      try {
        const response = await axios.get(path);
        this.categories = response.data.categories;
        this.loading = false;
      } catch (error) {
        this.errorMessage = 'An error Occured';
        this.loading = false;
      }
    },
    async addCategory(payload) {
      this.loading = true;
      const path = `${API_URL}/category`;
      try {
        await axios.post(path, payload);
        await this.getCategories();
        this.loading = false;
      } catch (error) {
        this.errorMessage = 'An error Occured';
        this.loading = false;
      }
    },
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown;
    },
    initForm() {
      this.addCategoryForm.category = '';
      this.addCategoryForm.description = '';
      this.addCategoryForm.words = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addCategoryModal.hide();
      const payload = {
        name: this.addCategoryForm.category,
        description: this.addCategoryForm.description,
        words: this.addCategoryForm.words.split(','),
      };
      this.addCategory(payload);
      this.initForm();
    },
    checkLetter(letter) {
      if (!this.startedGame) {
        this.errorMessage = 'Start Game first';
        this.dismissCountDown = this.dismissSecs;
        return;
      }
      let match = false;
      if (this.clicked.includes(letter)) {
        return;
      }
      this.clicked.push(letter);
      for (let i = 0; i < this.displayLetters.length; i += 1) {
        if (letter.toLowerCase() === this.wordLetters[i].toLowerCase()) {
          this.displayLetters.splice(i, 1, letter);
          match = true;
        }
      }
      if (!match) {
        this.strikes += 1;
        if (this.strikes > 10) {
          this.message = { msg: 'You Lost ....Play again', variant: 'danger' };
          this.lost = true;
          this.clicked = this.letters;
        }
      } else {
        this.correct += 1;
        const uniqueLetters = [...new Set(this.wordLetters)];
        if (this.correct >= uniqueLetters.length) {
          this.message = { msg: 'You Won ....Hurray', variant: 'success' };
          this.won = true;
          this.clicked = this.letters;
        }
      }
    },
    async selectCategory(category) {
      this.category = category;
      this.selectedCategory = true;
    },
    async startGame(category) {
      try {
        if (!this.selectedCategory) {
          this.errorMessage = 'Select a category';
          this.dismissCountDown = this.dismissSecs;
          return;
        }
        this.loading = true;
        const path = `${API_URL}/word?category_id=${category.id}`;
        const response = await axios.get(path);
        const { words } = response.data;
        const item = words[Math.floor(Math.random() * words.length)];
        this.word = item.word;
        this.startedGame = true;
        this.loading = false;
        this.initialize();
      } catch (error) {
        this.errorMessage = 'An error Occured';
      }
    },
    initialize() {
      this.strikes = 0;
      this.correct = 0;
      this.won = false;
      this.lost = false;
      this.displayLetters = Array(this.word.length);
      this.wordLetters = this.word.toUpperCase().split('');
      this.clicked = [];
      this.message = '';
    },
  },
  created() {
    this.getCategories();
  },
};
</script>

<style scoped>
.letter {
  display: inline-block;
  border-bottom: 1px solid;
  margin: 0px 3px 0px 3px;
  font-size: 30px;
  min-width: 30px;
  vertical-align: bottom;
}
</style>
