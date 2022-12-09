<template>
  <div class="blog-post">
    <div>
      <h1 class="blog-post-title">{{ blogPost.title }}</h1>
    </div>
    <p class="blog-post-description">{{ blogPost.description }}</p>
    <div class="article-div">
      <article class="article" v-html="blogPost.content"></article>
    </div>
    <span class="blog-post-delete" @click="deleteBlogPost">
      Удалить публикацию
      <img src="../../public/trash_bin.png" width="20" height="20" />
    </span>
  </div>
</template>

<script>
export default {
  name: "BlogPostComponent",
  props: {
    blogPost: {
      type: Object,
      required: true,
    },
  },
  methods: {
    deleteBlogPost() {
      fetch(`http://localhost:5000/blog-posts/${this.blogPost.id}`, {
        method: "DELETE",
      }).then((resp) => {
        if (resp.status === 204) {
          this.$router.push("/");
        }
      });
    },
  },
};
</script>

<style scoped>
.blog-post {
  border: 1px solid black;
  padding: 10px;
  margin: 10px;
  padding-bottom: 40px;
}

.article {
  text-align: center;
  max-width: 1200px;
}

.article-div {
  text-align: center;
  display: flex;
  justify-content: center;
}

.blog-post-title {
  font-size: 2rem;
  text-align: center;
}

.blog-post-description {
  font-size: 1.2rem;
  color: #666;
}

.blog-post-content {
  font-size: 1rem;
}

.blog-post-delete {
  float: right;
  display: block;
  text-align: center;
  color: #f00;
  cursor: pointer;
}
</style>
