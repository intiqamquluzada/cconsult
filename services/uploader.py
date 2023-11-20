class Uploader:

    @staticmethod
    def upload_photo_to_team(instance, filename):
        return f"teams/{filename}"
    
    
    @staticmethod
    def upload_photo_to_blog(instance, filename):
        return f"blogs/{instance.slug}/{filename}"
    
    @staticmethod
    def upload_photo_to_service(instance, filename):
        return f"services/{instance.slug}/{filename}"
    
    @staticmethod
    def upload_photo_to_about(instance, filename):
        return f"about/{filename}"
    
    @staticmethod
    def upload_photo_to_slider(instance, filename):
        return f"slider/{filename}"
    
    @staticmethod
    def upload_photo_to_logo(instance, filename):
        return f"logo/{filename}"