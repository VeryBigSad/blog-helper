<template>
  <div>
    <h2>Blog publications</h2>
    <p v-if="blogPosts.length === 0">Empty here...</p>
    <div>
      <div class="blog-post" v-for="blogPost in blogPosts" :key="blogPost.id">
        <BlogPostPreviewComponent :blogPost="blogPost" />
      </div>
    </div>
  </div>
</template>

<script>
import BlogPostPreviewComponent from "@/components/BlogPostPreviewComponent.vue";

export default {
  data() {
    return {
      blogPosts: [],
    };
  },
  created() {
    this.getBlogPosts();
  },
  methods: {
    getBlogPosts() {
      fetch("http://localhost:5000/blog-posts")
        .then((resp) => {
          resp.json().then((result) => {
            this.blogPosts = result;
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  components: { BlogPostPreviewComponent },
};
</script>

<style scoped>
/* display them in a 2-width grid (2 posts on each row) */
.blog-post {
  width: 50%;
  display: inline-block;
  vertical-align: top;
}
</style>
