/*
 * DATEX II Snapshot Pull API
 *
 * This is DATEX II Snapshot PULL API returning PayloadPublication.
 *
 * The version of the OpenAPI document: 1.0.2
 * Contact: you@your-company.com
 * Generated by: https://openapi-generator.tech
 */

using System;
using System.Linq;
using System.Text;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Org.OpenAPITools.Converters;

namespace Org.OpenAPITools.Models
{ 
        /// <summary>
        /// Gets or Sets HeightTypeEnum
        /// </summary>
        [TypeConverter(typeof(CustomEnumConverter<HeightTypeEnum>))]
        [JsonConverter(typeof(Newtonsoft.Json.Converters.StringEnumConverter))]
        public enum HeightTypeEnum
        {
            
            /// <summary>
            /// Enum EllipsoidalHeightEnum for ellipsoidalHeight
            /// </summary>
            [EnumMember(Value = "ellipsoidalHeight")]
            EllipsoidalHeightEnum = 1,
            
            /// <summary>
            /// Enum GravityRelatedHeightEnum for gravityRelatedHeight
            /// </summary>
            [EnumMember(Value = "gravityRelatedHeight")]
            GravityRelatedHeightEnum = 2,
            
            /// <summary>
            /// Enum RelativeHeightEnum for relativeHeight
            /// </summary>
            [EnumMember(Value = "relativeHeight")]
            RelativeHeightEnum = 3,
            
            /// <summary>
            /// Enum ExtendedGEnum for extendedG
            /// </summary>
            [EnumMember(Value = "extendedG")]
            ExtendedGEnum = 4
        }
}
