<template>
  <div>
    <BlogPostComponent :blogPost="blogPost" />
  </div>
</template>

<script>
import BlogPostComponent from "@/components/BlogPostComponent.vue";

export default {
  name: "BlogPostView",
  data() {
    return {
      blogPost: {},
    };
  },
  created() {
    this.getBlogPost();
  },
  methods: {
    getBlogPost() {
      fetch(`http://localhost:5000/blog-posts/${this.$route.params.id}`).then((resp) => {
          if (resp.status === 404) {
            this.$router.push("/");
          }
          resp.json().then((result) => {
            this.blogPost = result;
          });
        }
      );
    },
  },
  components: { BlogPostComponent }
};
</script>
