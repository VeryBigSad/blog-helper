<template>
  <div>
    <h1 v-if="creationStatus === -1">Create your blog post!</h1>
    <h1 v-else-if="creationStatus === 1">Creating your post... Please don't refresh the page!</h1>
    <div v-if="creationStatus === -1" class="blog-post-create-form">
      <label for="blog-post-title">Title</label>
      <input type="text" id="blog-post-title" v-model="blogPostTitle" />
      <label for="blog-post-description">Description</label>
      <!-- description input should be big -->
      <textarea
        v-model="blogPostDescription"
        id="blog-post-description"
        cols="30"
        rows="10"
      ></textarea>
      <input type="submit" value="Create" @click="createBlogPost" />
    </div>

  </div>
</template>

<script>
export default {
  name: "BlogPostCreateView",
  data() {
    return {
      blogPostTitle: "",
      blogPostDescription: "",
      creationStatus: -1,
    };
  },
  methods: {
    createBlogPost() {
      fetch("http://localhost:5000/blog-posts", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          title: this.blogPostTitle,
          description: this.blogPostDescription,
        }),
      }).then((resp) => {
        resp.json().then((result) => {
          this.$router.push(`/blog/${result.id}`);
        });
      });
      this.creationStatus = 1;
    },
  }
};
</script>

<style scoped>
.blog-post-create-form {
  display: flex;
  flex-direction: column;
  width: 50%;
  margin: 0 auto;
}

.blog-post-create-form label {
  margin-top: 10px;
}

.blog-post-create-form input {
  margin-top: 5px;
  padding: 5px;
}

.blog-post-create-form input[type="submit"] {
  margin-top: 10px;
  padding: 5px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.blog-post-create-form input[type="submit"]:hover {
  background-color: #45a049;
}

.blog-post-create-form input[type="submit"]:active {
  background-color: #3e8e41;
}

/* set max width of form to be small */

.blog-post-create-form {
  max-width: 400px;
}
/* style inputs and text areas */
.blog-post-create-form input,
.blog-post-create-form textarea {
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

</style>
