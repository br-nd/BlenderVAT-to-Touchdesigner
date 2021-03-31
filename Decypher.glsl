uniform sampler2D VAT_Pos;
uniform sampler2D VAT_Norm;
uniform float scale;
uniform float texture_width;
uniform float time;
uniform int numOfFrames;
uniform float frame;

out Vertex
{
	vec4 color;
	vec3 worldSpacePos;
	vec3 worldSpaceNorm;
	flat int cameraIndex;
} oVert;


void main() 
{
	float frame = clamp(time, 0.0, 0.99999) * numOfFrames;

	
	float pixel = 1.0 / texture_width;
	float half_pixel = pixel * 0.5;
	float frame_pixel_size = 1.0 / numOfFrames;
	
	float u = uv[1].x;
    float v = uv[1].y - (floor(frame) / numOfFrames);
    vec2 UV = vec2(u, v);	
	
	vec3 pos = texture(VAT_Pos, UV + vec2(half_pixel, -((frame + 0.5) * frame_pixel_size))).xyz;
	vec3 norm = texture(VAT_Norm, UV + vec2(half_pixel, -((frame + 0.5) * frame_pixel_size))).xyz;
	
	float new_x = (pos.x * 2.0) - 1.0;
	float new_y = ((pos.z * 2.0) - 1.0) * -1.0;
	float new_z = ((pos.y * 2.0) - 1.0);
	
	float norm_x = (norm.x * 2.0) - 1.0;
	float norm_y = ((norm.z * 2.0) - 1.0) * -1.0;
	float norm_z = ((norm.y * 2.0) - 1.0) ;
	
	norm = vec3(norm_x, norm_y, norm_z);	
	pos = vec3(new_x, new_y, new_z) * scale;
	
	vec4 worldSpacePos = TDDeform(pos);
	vec3 uvUnwrapCoord = TDInstanceTexCoord(TDUVUnwrapCoord());

	gl_Position = TDWorldToProj(worldSpacePos, uvUnwrapCoord);
	
	
	
#ifndef TD_PICKING_ACTIVE

	int cameraIndex = TDCameraIndex();
	oVert.cameraIndex = cameraIndex;
	oVert.worldSpacePos.xyz = worldSpacePos.xyz;
	
	// 色を設定
	oVert.color = TDInstanceColor(vec4(1,1,1,1));
	
	// 法線を設定
	vec3 worldSpaceNorm = normalize(TDDeformNorm(norm));
	
	oVert.worldSpaceNorm.xyz = worldSpaceNorm;

#else // TD_PICKING_ACTIVE

	TDWritePickingValues();

#endif // TD_PICKING_ACTIVE	
}



