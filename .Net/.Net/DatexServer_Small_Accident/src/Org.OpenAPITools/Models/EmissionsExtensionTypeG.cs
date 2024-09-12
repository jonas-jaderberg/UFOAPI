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
    /// 
    /// </summary>
    [DataContract]
    public partial class EmissionsExtensionTypeG : IEquatable<EmissionsExtensionTypeG>
    {
        /// <summary>
        /// Gets or Sets EmissionsExtension
        /// </summary>
        [DataMember(Name="EmissionsExtension", EmitDefaultValue=false)]
        public EmissionsExtension EmissionsExtension { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class EmissionsExtensionTypeG {\n");
            sb.Append("  EmissionsExtension: ").Append(EmissionsExtension).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="obj">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object obj)
        {
            if (obj is null) return false;
            if (ReferenceEquals(this, obj)) return true;
            return obj.GetType() == GetType() && Equals((EmissionsExtensionTypeG)obj);
        }

        /// <summary>
        /// Returns true if EmissionsExtensionTypeG instances are equal
        /// </summary>
        /// <param name="other">Instance of EmissionsExtensionTypeG to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(EmissionsExtensionTypeG other)
        {
            if (other is null) return false;
            if (ReferenceEquals(this, other)) return true;

            return 
                (
                    EmissionsExtension == other.EmissionsExtension ||
                    EmissionsExtension != null &&
                    EmissionsExtension.Equals(other.EmissionsExtension)
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                var hashCode = 41;
                // Suitable nullity checks etc, of course :)
                    if (EmissionsExtension != null)
                    hashCode = hashCode * 59 + EmissionsExtension.GetHashCode();
                return hashCode;
            }
        }

        #region Operators
        #pragma warning disable 1591

        public static bool operator ==(EmissionsExtensionTypeG left, EmissionsExtensionTypeG right)
        {
            return Equals(left, right);
        }

        public static bool operator !=(EmissionsExtensionTypeG left, EmissionsExtensionTypeG right)
        {
            return !Equals(left, right);
        }

        #pragma warning restore 1591
        #endregion Operators
    }
}
